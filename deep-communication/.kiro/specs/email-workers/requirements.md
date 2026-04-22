# Requirements Document

## Introduction

This feature implements a set of Cloudflare Workers that serve as the API and public-facing layer for an email campaign management system. The Workers connect to an existing PostgreSQL database (with tables `email_list`, `email_list_subscriber`, `email_campaign`, `email_campaign_send`, and `email_opt_out`) and provide CRUD operations for managing lists, subscribers, and campaigns, a browser-viewable version of campaign emails, and an unsubscribe flow for recipients. The Workers are deployed using the Cloudflare account credentials already present in the project's `.env` file.

## Glossary

- **Worker**: A Cloudflare Worker — a serverless JavaScript function deployed to Cloudflare's edge network
- **API_Worker**: The Cloudflare Worker that exposes the JSON REST API for managing email lists, subscribers, campaigns, and campaign sends
- **Public_Worker**: The Cloudflare Worker (or set of routes on the same Worker) that serves public-facing pages — the campaign browser view and the unsubscribe flow
- **Email_List**: A mailing list record in the `email_list` table
- **Subscriber**: A record in the `email_list_subscriber` table linking an email address to an Email_List
- **Campaign**: A record in the `email_campaign` table representing a single email campaign with subject, HTML body, and text body
- **Campaign_Send**: A record in the `email_campaign_send` table tracking the delivery status of a Campaign to a single recipient
- **Opt_Out**: A record in the `email_opt_out` table representing a global opt-out for an email address
- **Browser_View**: An HTML page served by the Worker that renders a Campaign's `body_html` for viewing in a web browser
- **Unsubscribe_Page**: An HTML page served by the Worker that allows a recipient to unsubscribe from a list or globally opt out
- **Database_Connection**: A PostgreSQL connection from the Worker to the existing database, established using a connection string stored as a Cloudflare secret
- **API_Key**: A shared secret stored as a Cloudflare Worker secret (`API_KEY`) and required in the `X-API-Key` request header for all `/api/*` routes

## Requirements

### Requirement 1: Email List CRUD

**User Story:** As a campaign manager, I want to create, read, update, and delete email lists through an API, so that I can organize my subscribers into targeted groups.

#### Acceptance Criteria

1. WHEN a POST request with a valid `name` and optional `description` is received at `/api/lists`, THE API_Worker SHALL insert a new Email_List record and return the created record with HTTP status 201.
2. WHEN a GET request is received at `/api/lists`, THE API_Worker SHALL return all Email_List records as a JSON array with HTTP status 200.
3. WHEN a GET request is received at `/api/lists/:id` with a valid Email_List id, THE API_Worker SHALL return the matching Email_List record with HTTP status 200.
4. WHEN a PUT request with updated fields is received at `/api/lists/:id` with a valid Email_List id, THE API_Worker SHALL update the Email_List record, set `updated_at` to the current timestamp, and return the updated record with HTTP status 200.
5. WHEN a DELETE request is received at `/api/lists/:id` with a valid Email_List id, THE API_Worker SHALL delete the Email_List record and return HTTP status 204.
6. IF a GET, PUT, or DELETE request references an Email_List id that does not exist, THEN THE API_Worker SHALL return HTTP status 404 with a JSON error message.
7. IF a POST or PUT request is missing the required `name` field, THEN THE API_Worker SHALL return HTTP status 400 with a JSON validation error message.

### Requirement 2: Subscriber Management

**User Story:** As a campaign manager, I want to add, view, update, and remove subscribers from email lists, so that I can maintain accurate recipient lists.

#### Acceptance Criteria

1. WHEN a POST request with a valid `email` is received at `/api/lists/:id/subscribers`, THE API_Worker SHALL insert a new Subscriber record linked to the specified Email_List and return the created record with HTTP status 201.
2. WHEN a GET request is received at `/api/lists/:id/subscribers`, THE API_Worker SHALL return all Subscriber records for the specified Email_List as a JSON array with HTTP status 200.
3. WHEN a DELETE request is received at `/api/lists/:id/subscribers/:subscriberId`, THE API_Worker SHALL delete the Subscriber record and return HTTP status 204.
4. IF a POST request provides an email that already exists for the specified Email_List, THEN THE API_Worker SHALL return HTTP status 409 with a JSON error message indicating the duplicate.
5. IF a POST request provides an email address that exists in the Opt_Out table, THEN THE API_Worker SHALL return HTTP status 422 with a JSON error message indicating the email has globally opted out.
6. IF the referenced Email_List id does not exist, THEN THE API_Worker SHALL return HTTP status 404 with a JSON error message.

### Requirement 3: Campaign CRUD

**User Story:** As a campaign manager, I want to create, read, update, and delete email campaigns, so that I can prepare and manage my email content.

#### Acceptance Criteria

1. WHEN a POST request with a valid `name`, `subject`, and optional `body_html`, `body_text`, `email_list_id`, and `scheduled_at` is received at `/api/campaigns`, THE API_Worker SHALL insert a new Campaign record with status `draft` and return the created record with HTTP status 201.
2. WHEN a GET request is received at `/api/campaigns`, THE API_Worker SHALL return all Campaign records as a JSON array with HTTP status 200.
3. WHEN a GET request is received at `/api/campaigns/:id` with a valid Campaign id, THE API_Worker SHALL return the matching Campaign record with HTTP status 200.
4. WHEN a PUT request with updated fields is received at `/api/campaigns/:id` with a valid Campaign id, THE API_Worker SHALL update the Campaign record, set `updated_at` to the current timestamp, and return the updated record with HTTP status 200.
5. WHEN a DELETE request is received at `/api/campaigns/:id` with a valid Campaign id, THE API_Worker SHALL delete the Campaign record and return HTTP status 204.
6. IF a GET, PUT, or DELETE request references a Campaign id that does not exist, THEN THE API_Worker SHALL return HTTP status 404 with a JSON error message.
7. IF a POST or PUT request is missing the required `name` or `subject` field, THEN THE API_Worker SHALL return HTTP status 400 with a JSON validation error message.
8. IF a POST or PUT request references an `email_list_id` that does not exist, THEN THE API_Worker SHALL return HTTP status 422 with a JSON error message.

### Requirement 4: Campaign Send Tracking

**User Story:** As a campaign manager, I want to view and manage per-recipient send records for a campaign, so that I can track delivery status.

#### Acceptance Criteria

1. WHEN a GET request is received at `/api/campaigns/:id/sends`, THE API_Worker SHALL return all Campaign_Send records for the specified Campaign as a JSON array with HTTP status 200.
2. WHEN a GET request is received at `/api/campaigns/:id/sends/:sendId`, THE API_Worker SHALL return the matching Campaign_Send record with HTTP status 200.
3. IF the referenced Campaign id does not exist, THEN THE API_Worker SHALL return HTTP status 404 with a JSON error message.

### Requirement 5: Campaign Browser View

**User Story:** As an email recipient, I want to view the HTML version of a campaign email in my web browser, so that I can read the email if my email client does not render it properly.

#### Acceptance Criteria

1. WHEN a GET request is received at `/view/:campaignId`, THE Public_Worker SHALL query the Campaign record and return the `body_html` content as a full HTML page with Content-Type `text/html` and HTTP status 200.
2. IF the Campaign `body_html` field is empty or null, THEN THE Public_Worker SHALL return the `body_text` content wrapped in a basic HTML template with Content-Type `text/html` and HTTP status 200.
3. IF the referenced Campaign id does not exist, THEN THE Public_Worker SHALL return an HTML error page with HTTP status 404.
4. THE Public_Worker SHALL inject an unsubscribe link into the rendered browser view page that points to the Unsubscribe_Page.

### Requirement 6: Unsubscribe Flow

**User Story:** As an email recipient, I want to unsubscribe from a mailing list or opt out globally, so that I stop receiving unwanted emails.

#### Acceptance Criteria

1. WHEN a GET request is received at `/unsubscribe` with query parameters `email` and `list_id`, THE Public_Worker SHALL render an HTML Unsubscribe_Page showing the subscriber's email and options to unsubscribe from the specific list or opt out globally.
2. WHEN the Unsubscribe_Page form is submitted with the "unsubscribe from list" option, THE Public_Worker SHALL update the Subscriber record's status to `unsubscribed`, set `unsubscribed_at` to the current timestamp, and render a confirmation page.
3. WHEN the Unsubscribe_Page form is submitted with the "opt out globally" option, THE Public_Worker SHALL insert a record into the Opt_Out table, update all Subscriber records for that email to status `unsubscribed`, and render a confirmation page.
4. IF the `email` or `list_id` query parameter is missing from the GET request, THEN THE Public_Worker SHALL return an HTML error page with HTTP status 400.
5. IF the Subscriber record for the given email and list does not exist, THEN THE Public_Worker SHALL still allow global opt-out and render the page with only the global opt-out option.
6. IF the email already exists in the Opt_Out table when a global opt-out is submitted, THEN THE Public_Worker SHALL render the confirmation page without inserting a duplicate record.

### Requirement 7: Database Connectivity

**User Story:** As a developer, I want the Worker to connect to the existing PostgreSQL database securely, so that all data operations use the established schema.

#### Acceptance Criteria

1. THE Worker SHALL connect to the PostgreSQL database using a connection string provided via a Cloudflare Worker secret named `DATABASE_URL`.
2. THE Worker SHALL use parameterized queries for all database operations to prevent SQL injection.
3. IF the database connection fails, THEN THE Worker SHALL return HTTP status 503 with a JSON error message indicating a service unavailability.

### Requirement 8: API Authentication

**User Story:** As a developer, I want the admin API endpoints protected by an API key, so that only authorized clients can manage email lists, subscribers, and campaigns, while public-facing pages remain accessible to email recipients.

#### Acceptance Criteria

1. THE API_Worker SHALL require a valid API key in the `X-API-Key` request header for all routes under `/api/*`.
2. THE API key SHALL be stored as a Cloudflare Worker secret named `API_KEY` and configured via `wrangler secret put API_KEY`.
3. IF a request to any `/api/*` route is missing the `X-API-Key` header, THEN THE API_Worker SHALL return HTTP status 401 with a JSON error message `{"error": "Missing API key"}`.
4. IF a request to any `/api/*` route provides an `X-API-Key` header value that does not match the stored `API_KEY` secret, THEN THE API_Worker SHALL return HTTP status 403 with a JSON error message `{"error": "Invalid API key"}`.
5. THE API_Worker SHALL compare the API key using a constant-time comparison to prevent timing attacks.
6. THE Public_Worker routes (`/view/:campaignId`, `/unsubscribe`) SHALL NOT require any authentication and SHALL remain publicly accessible.

### Requirement 9: Request Validation and Error Handling

**User Story:** As a developer, I want consistent error handling across all API endpoints, so that clients receive predictable error responses.

#### Acceptance Criteria

1. THE API_Worker SHALL return all error responses as JSON objects with a `error` field containing a human-readable message.
2. IF a request is received with an unsupported HTTP method for a given route, THEN THE API_Worker SHALL return HTTP status 405.
3. IF a request body contains malformed JSON, THEN THE API_Worker SHALL return HTTP status 400 with a JSON error message.
4. THE API_Worker SHALL set the `Content-Type` header to `application/json` for all JSON responses.
5. THE API_Worker SHALL set appropriate CORS headers to allow cross-origin requests from any origin.

### Requirement 10: Worker Deployment Configuration

**User Story:** As a developer, I want a properly configured `wrangler.toml` and project structure, so that I can deploy the Worker to Cloudflare using the existing account credentials.

#### Acceptance Criteria

1. THE Worker project SHALL include a `wrangler.toml` configuration file specifying the worker name, compatibility date, and account id.
2. THE Worker project SHALL use the Cloudflare Account ID from the environment for deployment.
3. THE Worker project SHALL include a `package.json` with the required dependencies for the Cloudflare Workers runtime and PostgreSQL client.
