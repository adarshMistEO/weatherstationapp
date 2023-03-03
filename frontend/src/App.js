import './App.css';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { Login } from './components/auth/Login';
import { Homepage } from './components/Dashboard/Homepage';

function App() {
  return <BrowserRouter>
    <Routes>
      <Route path="/login" element={<Login/>} />
      <Route path="/dashboard" element={<Homepage/>} />
    </Routes>

  </BrowserRouter>
}

export default App;
