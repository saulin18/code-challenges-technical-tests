import { createContext, useContext, useState, useEffect, useCallback } from "react";
import type { User } from "./types";

type AuthContextType = {
accessToken: string;
refreshToken: string;
user: User | null;
    setAuth: (accessToken: string, refreshToken: string) => void;
    clearAuth: () => void;
}

// Decodificar JWT para obtener información del usuario
const decodeJWT = (token: string): { id: string; email: string; role: string; status: string } | null => {
    try {
        const base64Url = token.split('.')[1];
        const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
        const jsonPayload = decodeURIComponent(atob(base64).split('').map((c) => {
            return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
        }).join(''));
        return JSON.parse(jsonPayload);
    } catch (error) {
        return null;
    }
};


const AuthContext = createContext<AuthContextType>({
    accessToken: "",
    refreshToken: "",
    user: null,
    setAuth: () => {},
    clearAuth: () => {},
});

export const AuthProvider = ({ children }: { children: React.ReactNode }) => {
    const initialToken = localStorage.getItem("accessToken") || "";
    const initialRefreshToken = localStorage.getItem("refreshToken") || "";
    console.log("🔵 [AUTH] Initializing AuthProvider");
    console.log("🔵 [AUTH] Initial token from localStorage:", initialToken ? "EXISTS" : "NOT FOUND");
    
    const [accessToken, setAccessToken] = useState<string>(initialToken);
    const [refreshToken, setRefreshToken] = useState<string>(initialRefreshToken);
    const [user, setUser] = useState<User | null>(null);
    
    console.log("🔵 [AUTH] State initialized - accessToken:", accessToken ? "EXISTS" : "NOT FOUND");

    // Cargar usuario cuando hay un token
    useEffect(() => {
        const loadUser = () => {
            console.log("🔵 [AUTH] Loading user, accessToken exists:", !!accessToken);
            if (!accessToken) {
                console.log("🔴 [AUTH] No access token, setting user to null");
                setUser(null);
                return;
            }

            const decoded = decodeJWT(accessToken);
            console.log("🔵 [AUTH] Decoded JWT:", decoded);
            if (!decoded || !decoded.id) {
                console.log("🔴 [AUTH] Failed to decode JWT or no id found");
                setUser(null);
                return;
            }

            // Construir usuario desde el JWT (no necesitamos llamar al backend)
            // Para crear tareas solo necesitamos el id, que ya lo tenemos
            const userFromJWT: User = {
                id: decoded.id,
                email: decoded.email,
                firstName: "", // No está en el JWT, pero no es necesario para crear tareas
                lastName: "", // No está en el JWT, pero no es necesario para crear tareas
                role: decoded.role,
                status: decoded.status,
                createdAt: new Date().toISOString(), // Placeholder
                updatedAt: new Date().toISOString(), // Placeholder
            };
            
            console.log("🔵 [AUTH] User from JWT:", userFromJWT);
            setUser(userFromJWT);
        };

        loadUser();
    }, [accessToken]);

    const setAuth = useCallback((newAccessToken: string, newRefreshToken: string) => {
        console.log("🔵 [AUTH] setAuth called with token:", newAccessToken ? "EXISTS" : "NOT FOUND");
        localStorage.setItem("accessToken", newAccessToken);
        localStorage.setItem("refreshToken", newRefreshToken);
        setAccessToken(newAccessToken);
        setRefreshToken(newRefreshToken);
        console.log("🔵 [AUTH] Token saved, useEffect should trigger");
        // El useEffect se ejecutará automáticamente para cargar el usuario
    }, []);

    const clearAuth = useCallback(() => {
        localStorage.removeItem("accessToken");
        localStorage.removeItem("refreshToken");
        setAccessToken("");
        setRefreshToken("");
        setUser(null);
    }, []);

    return (
        <AuthContext.Provider value={{
            accessToken,
            refreshToken,
            user,
            setAuth,
            clearAuth,
        }}>
        {children}
        </AuthContext.Provider>
    );
};

export const useAuthContext = () => {
    const context = useContext(AuthContext);
    if (!context) {
        throw new Error("useAuthContext must be used within an AuthProvider");
    }
    return context;
};
