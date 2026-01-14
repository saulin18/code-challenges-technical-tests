import { authService } from "@/features/auth/auth-service";
import { describe, it, expect, beforeAll } from "vitest";
import { getApiUrl } from "@/common/api-config";


describe("Auth Service Integration Tests", () => {

  const generateUniqueEmail = (prefix: string) => {
    return `${prefix}-${Date.now()}-${Math.random().toString(36).substring(7)}@test.com`;
  };

  
  beforeAll(async () => {
    try {
      const response = await fetch(getApiUrl("/health"), {
        method: "GET",
        signal: AbortSignal.timeout(5000), 
      });
      if (!response.ok && response.status >= 500) {
        throw new Error(`Backend no disponible: ${response.status}`);
      }
    } catch (error: any) {
      if (error.name === "AbortError") {
        throw new Error(
          "Backend no responde. Asegúrate de que el servidor esté corriendo en " +
            getApiUrl("")
        );
      }
      if (error.message?.includes("fetch") || error.code === "ECONNREFUSED") {
        throw new Error(
          `No se puede conectar al backend en ${getApiUrl("")}. ` +
            "Asegúrate de que el servidor esté corriendo."
        );
      }
    }
  });

  describe("register", () => {
    it("should register successfully with valid data", async () => {
      const uniqueEmail = generateUniqueEmail("newuser");
      const result = await authService().register(
        uniqueEmail,
        "testpassword123",
        "Test",
        "User"
      );

      if (!result.ok) {
        console.error("Register failed:", result.error);
      }

      expect(result.ok).toBeTruthy();
      if (result.ok) {
        expect(result.data.accessToken).toBeDefined();
        expect(result.data.refreshToken).toBeDefined();
      }
    });

    it("should fail register with existing email", async () => {
      const uniqueEmail = generateUniqueEmail("existing");
      
      const registerResult = await authService().register(
        uniqueEmail,
        "testpassword123",
        "Test",
        "User"
      );
      
      expect(registerResult.ok).toBeTruthy();

      const duplicateResult = await authService().register(
        uniqueEmail,
        "testpassword123",
        "Test",
        "User"
      );

      expect(duplicateResult.ok).toBeFalsy();
      if (!duplicateResult.ok) {
        expect(duplicateResult.error).toBeDefined();
        expect(duplicateResult.error.message).toBeDefined();
      }
    });
  });

  describe("login", () => {
    it("should login successfully with valid credentials", async () => {
      const uniqueEmail = generateUniqueEmail("login");
      const password = "testpassword123";

      const registerResult = await authService().register(
        uniqueEmail,
        password,
        "Test",
        "User"
      );

      if (!registerResult.ok) {
        console.error("Register failed before login:", registerResult.error);
        throw new Error(`Failed to register user: ${registerResult.error.message}`);
      }

      const result = await authService().login(uniqueEmail, password);

      if (!result.ok) {
        console.error("Login failed:", result.error);
      }

      expect(result.ok).toBeTruthy();
      if (result.ok) {
        expect(result.data.accessToken).toBeDefined();
        expect(result.data.refreshToken).toBeDefined();
      }
    });

    it("should fail login with invalid credentials", async () => {
      const result = await authService().login(
        "invalid@test.com",
        "wrongpassword"
      );

      expect(result.ok).toBeFalsy();
      if (!result.ok) {
        expect(result.error).toBeDefined();
        expect(result.error.message).toBeDefined();
      }
    });
  });
});
