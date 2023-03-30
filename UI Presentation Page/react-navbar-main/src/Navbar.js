import { Link, useMatch, useResolvedPath } from "react-router-dom";

export default function Navbar() {
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
          <CustomLink to="/help">Help</CustomLink>
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
