import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000/api";

export const getTeams = async () => {
  const response = await axios.get(`${API_URL}/teams/`);
  return response.data;
};

export const getTournaments = async () => {
  const response = await axios.get(`${API_URL}/tournaments/`);
  return response.data;
};
