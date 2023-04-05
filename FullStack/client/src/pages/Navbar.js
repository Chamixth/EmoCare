import { Link, useMatch, useResolvedPath, useNavigate } from "react-router-dom";
import { useState } from "react";

export default function Navbar() {
  const Navigate = useNavigate();
  const [isOpen, setIsOpen] = useState(false);

  function toggleMenu() {
    setIsOpen(!isOpen);
  }

  return (
    <div className="navbar-wrapper">
      <nav className="nav-1">
        <Link to="/" className="site-title">
          <p class="logo">
            <span>Emo</span>Care
          </p>
        </Link>
        <button className="navbar-toggle" onClick={toggleMenu}>
          <span className="navbar-toggle-icon">&#9776;</span>
        </button>
        <ul className={`navbar-menu ${isOpen ? "navbar-menu-open" : ""}`}>
          <CustomLink to="/">Home</CustomLink>
          <CustomLink to="/about">About Us</CustomLink>
          <CustomLink to="/help">Services</CustomLink>
          <button
            className="navbar-button-1"
            onClick={() => Navigate("/login")}
          >
            SIGN IN{" "}
          </button>
          <button className="navbar-button-2" onClick={() => Navigate("/sign")}>
            SIGN UP{" "}
          </button>
        </ul>
      </nav>
    </div>
  );
}

function CustomLink({ to, children, ...props }) {
  const resolvedPath = useResolvedPath(to);
  const isActive = useMatch({ path: resolvedPath.pathname, end: true });

  return (
    <li className={isActive ? "active" : ""}>
      <Link to={to} {...props}>
        {children}
      </Link>
    </li>
  );
}
