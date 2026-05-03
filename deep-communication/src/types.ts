export interface Env {
  DATABASE_URL: string;
  API_KEY: string;
  HYPERDRIVE?: Hyperdrive;
}

export interface EmailList {
  id: number;
  name: string;
  description: string | null;
  created_at: Date;
  updated_at: Date;
}

export interface EmailListSubscriber {
  id: number;
  email: string;
  email_list_id: number;
  status: string;
  subscribed_at: Date;
  unsubscribed_at: Date | null;
  unsubscribe_reason: string | null;
}

export interface EmailCampaign {
  id: number;
  name: string;
  subject: string;
  body_html: string | null;
  body_text: string | null;
  email_list_id: number | null;
  status: string;
  scheduled_at: Date | null;
  sent_at: Date | null;
  created_at: Date;
  updated_at: Date;
}

export interface EmailCampaignSend {
  id: number;
  email_campaign_id: number;
  email: string;
  status: string;
  sent_at: Date | null;
  delivered_at: Date | null;
  opened_at: Date | null;
  clicked_at: Date | null;
  bounced_at: Date | null;
  view_url: string | null;
  created_at: Date;
}

export interface EmailOptOut {
  id: number;
  email: string;
  reason: string | null;
  opted_out_at: Date;
}

export interface Banner {
  id: number;
  title: string | null;
  subtitle: string | null;
  image_url: string | null;
  url: string | null;
  type: "standard" | "minimal" | "transient";
  is_active: boolean;
  created_at: Date;
}

export interface UserBanner {
  id: number;
  user_uid: string;
  banner_id: number;
  max_expiration_date: Date;
  first_shown_expiration_hours: number | null;
  first_shown_at: Date | null;
  display_order: number | null;
  is_dismissed: boolean;
  created_at: Date;
}
