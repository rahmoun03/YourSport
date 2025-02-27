import { Routes, Route } from "react-router-dom";
import Home from "../pages/Home";
import Teams from "../pages/Teams";
import Tournaments from "../pages/Tournaments";
import Login from "../pages/Login";
import SignUp from "../pages/SignUp";

const AppRouter = () => {
  return (
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/teams" element={<Teams />} />
        <Route path="/tournaments" element={<Tournaments />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/login" element={<Login />} />
      </Routes>
  );
};

export default AppRouter;
