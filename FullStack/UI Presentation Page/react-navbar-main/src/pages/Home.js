import React from "react";
import BannerImage from "../Assets/home-banner-image.png";
import { useNavigate } from "react-router-dom";

const Home = () => {
  const Navigate = useNavigate();
  return (
    <div className="home-container">
      <div className="home-banner-container">
        <div className="home-text-section">
          <h1 className="primary-heading">Do you Know?</h1>
          <p className="primary-text">
            Social anxiety is an intense fear of social situations due to the
            fear of being judged or rejected. It can cause discomfort, avoidance
            of social interactions, and symptoms such as sweating and panic.
            Effective treatments are available. Let's experiment about your
            situation.
          </p>
          <button
            className="secondary-button-1"
            onClick={() => Navigate("/login")}
          >
            Start{" "}
          </button>
        </div>
        <div className="home-image-section">
          <img src={BannerImage} alt="" />
        </div>
      </div>
    </div>
  );
};

export default Home;
