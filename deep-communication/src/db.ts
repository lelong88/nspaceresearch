import { Client } from "pg";
import type { Env } from "./types";

export class DatabaseConnectionError extends Error {
  constructor(message: string, cause?: unknown) {
    super(message);
    this.name = "DatabaseConnectionError";
    this.cause = cause;
  }
}

export async function getClient(env: Env): Promise<Client> {
  const connectionString =
    env.HYPERDRIVE?.connectionString ?? env.DATABASE_URL;
  const client = new Client({ connectionString });

  try {
    await client.connect();
  } catch (err) {
    throw new DatabaseConnectionError("Failed to connect to database", err);
  }

  return client;
}
