import { Link, useMatch, useResolvedPath, useNavigate } from "react-router-dom";

export default function Navbar() {
  const Navigate = useNavigate();
  return (
    <div className="navbar-wrapper">
      <nav className="nav">
        <Link to="/" className="site-title">
          <p class="logo">
            <span>Emo</span>Care
          </p>
        </Link>
        <ul>
          <CustomLink to="/">Home</CustomLink>
          <CustomLink to="/about">About</CustomLink>
          <CustomLink to="/help">Services</CustomLink>
          <button
            className="navbar-button-1"
            onClick={() => Navigate("/login")}
          >
            LOG IN{" "}
          </button>
          <button className="navbar-button-2" onClick={() => Navigate("/sign")}>
            SIGN IN{" "}
          </button>
        </ul>
      </nav>
      <footer className="footer"></footer>
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
