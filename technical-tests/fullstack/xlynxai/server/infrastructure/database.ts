import { drizzle } from "drizzle-orm/node-postgres";
import * as schema from "./models/models";
import { loadEnvFile } from "node:process";

loadEnvFile('./.env');

if (!process.env.DATABASE_URL) {
    throw new Error("DATABASE_URL environment variable is not set");
}

export const db = drizzle(process.env.DATABASE_URL, { schema });
export type AppDatabase = typeof db;