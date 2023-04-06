import React from "react";
import BannerImage from "../Assets/home-banner-image.png";
import { useNavigate } from "react-router-dom";
import '../style.css'
import Navbar from "./Navbar";

const Home = () => {
  const Navigate = useNavigate();
  
  return (
    <>
      < Navbar />
    
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
            onClick={() => Navigate("/signin")}
          >
            Start{" "}
          </button>
        </div>
        <div className="home-image-section">
          <img className="card" src={BannerImage} alt="" />
        </div>
      </div>
    </div>
    </>
  );
};

export default Home;
