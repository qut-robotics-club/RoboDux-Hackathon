import React from "react";
import { Link } from "react-router-dom";

import Nav from "./Desiner";

// the header
export default function header() {
  return (
    <header>
      <Link to="/"></Link>
      <Nav />
    </header>
  );
}