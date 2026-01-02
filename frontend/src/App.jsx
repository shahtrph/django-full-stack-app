import { useState } from "react";
import { Routes, Route } from "react-router";
import Home from "./components/home";
import Create from "./components/create";
import Delete from "./components/delete";
import Edit from "./components/edit";
import Navbar from "./components/navbar/navbar";
import "./App.css";

function App() {
  return (
    <>
      <Navbar
        content={
          <Routes>
            <Route path="" element={<Home />} />
            <Route path="/create" element={<Create />} />
            <Route path="/edit/:id" element={<Edit />} />
            <Route path="/delete/:id" element={<Delete />} />
          </Routes>
        }
      />
    </>
  );
}

export default App;
