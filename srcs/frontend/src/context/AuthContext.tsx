import { createContext, useContext, useState, ReactNode } from "react";

// Define types for AuthContext
interface AuthContextType {
  isAuthenticated: boolean;
  login: () => void;
  logout: () => void;
}

// Create AuthContext
const AuthContext = createContext<AuthContextType | undefined>(undefined);

// AuthProvider Component
export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(
    !!localStorage.getItem("authToken") // Check if user is logged in
  );

  const login = () => {
    setIsAuthenticated(true);
    localStorage.setItem("authToken", "your_token_here"); // Store token
  };

  const logout = () => {
    setIsAuthenticated(false);
    localStorage.removeItem("authToken"); // Remove token
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

// Custom hook to use AuthContext
export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return context;
};
