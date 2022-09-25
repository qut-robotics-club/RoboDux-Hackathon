import React from "react";
import { StrictMode } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

// components
import Header from "./Design_pages/Header";
import Footer from "./Design_pages/Footer";

// pages
import Home from "./Design_pages/Home";


// styles
import "./css_file/first.css";
import "./css_file/other.css";


export default function App() {
  return (
    <StrictMode>
      <Router>
        <Header />        
        <Routes>
          <Route path="/" element={<Home />} />

        </Routes>
        <Footer />
      </Router>
    </StrictMode>
  );
}
