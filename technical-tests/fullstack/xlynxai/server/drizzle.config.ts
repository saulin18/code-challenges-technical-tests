import 'dotenv/config';
import { defineConfig } from 'drizzle-kit';

export default defineConfig({
  out: './drizzle',
  schema: './infrastructure/models/models.ts',
  dialect: 'postgresql',
  dbCredentials: {
    url: process.env.POSTGRES_URL || process.env.DATABASE_URL || 'postgresql://postgres:postgres@localhost:5432/postgres',
      },
});
