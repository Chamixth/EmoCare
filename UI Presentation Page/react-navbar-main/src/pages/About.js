import React from "react";
import AboutBackgroundImage from "../Assets/about-background-image.png";

const About = () => {
  return (
    <div className="about-section-container">
      <div className="about-section-image-container">
        <img src={AboutBackgroundImage} alt="" />
      </div>
      <div className="about-section-text-container">
        <p className="primary-subheading"></p>
        <h1 className="primary-heading">What does EmoCare provide.</h1>
        <p className="primary-text">
          What is online therapy? Online therapy is the provision of
          professional mental health counseling via the internet, usually
          through live video chat, messaging app, email, or over the phone.
        </p>
        <p className="primary-text">
          Faithful Counseling is designed as a solution for people seeking
          traditional mental health therapy who would prefer hearing from the
          perspective of a Christian. If you are seeking a mental health
          professional who is a practicing Christian, Faithful Counseling may be
          a great option for you.
        </p>
        <div className="about-buttons-container">
          <button className="secondary-button">Learn More</button>
        </div>
      </div>
    </div>
  );
};

export default About;
