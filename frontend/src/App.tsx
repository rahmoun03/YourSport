import AppRouter from "./routes/AppRouter";
import Navbar from "./components/Navbar";

function App() {
  return (
    <div className="min-h-screen bg-gray-100 text-gray-900">
      <Navbar />
      <AppRouter />
    </div>
  );
}

export default App;
