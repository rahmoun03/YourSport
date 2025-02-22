import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "../pages/Home";
import Teams from "../pages/Teams";
import Tournaments from "../pages/Tournaments";

const AppRouter = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/teams" element={<Teams />} />
        <Route path="/tournaments" element={<Tournaments />} />
      </Routes>
    </Router>
  );
};

export default AppRouter;
