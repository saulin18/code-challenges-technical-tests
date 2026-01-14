
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export const getApiUrl = (path: string) => {
    return `${API_URL}${path}`;
};