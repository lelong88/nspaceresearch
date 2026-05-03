import { Client } from "pg";
import type { Env } from "./types";

export async function getClient(env: Env): Promise<Client> {
  const client = new Client({
    connectionString: env.HYPERDRIVE.connectionString,
  });
  await client.connect();
  return client;
}

export async function query<T>(client: Client, sql: string, params: unknown[] = []): Promise<T[]> {
  const result = await client.query(sql, params);
  return result.rows as T[];
}
