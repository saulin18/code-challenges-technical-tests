
import express from "express";
import { loadEnvFile } from "node:process";
import { tasksRoutes } from "./api/routes/tasks/tasks.routes";
import { userRoutes } from "./api/routes/users/user.routes";
import { globalErrorHandler } from "./api/middlewares/global-error-handler";
import cors from "cors";

loadEnvFile('./.env')

export const app = express();
const port = process.env.PORT || 8000;

app.use(express.json());
app.use(cors());

app.use("/api/tasks", tasksRoutes);
app.use("/api/users", userRoutes);

app.get("/health", (req, res) => {
    res.status(200).json({ message: "OK" });
});

app.use(globalErrorHandler);

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`);
});