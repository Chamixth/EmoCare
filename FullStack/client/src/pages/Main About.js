import React from "react";
import Member1 from "../Assets/member1.png";
import Member2 from "../Assets/member2.png";
import Member3 from "../Assets/member3.png";
import Member4 from "../Assets/member4.png";
import Member5 from "../Assets/member5.png";
import Navbar from "./Navbar";

const About = () => {
  return (
    <>
      < Navbar />

    <div className="about-section-container">
      <div class="container-1">
        <div class="header">
          <h1>Our Team</h1>
        </div>
        <div class="members">
          <div class="member">
            <div class="image">
              <img src={Member1} alt="" />
            </div>
            <div class="name-member">
              <h3>Chamith Weerasinghe</h3>
            </div>
            <div class="pro">
              <button className="numb">w1899316</button>
            </div>
          </div>
          <div class="member">
            <div class="image">
              <img src={Member2} alt="" />
            </div>
            <div class="name-member">
              <h3>Sathmi Jayarathne</h3>
            </div>
            <div class="pro">
              <button className="numb">w1899311</button>
            </div>
          </div>
          <div class="member">
            <div class="image">
              <img src={Member3} alt="" />
            </div>
            <div class="name-member">
              <h3>Navod Dilshan</h3>
            </div>
            <div class="pro">
              <button className="numb">w1899300</button>
            </div>
          </div>
          <div class="member">
            <div class="image">
              <img src={Member4} alt="" />
            </div>
            <div class="name-member">
              <h3>Yasara Kithmini</h3>
            </div>
            <div class="pro">
              <button className="numb">w1000000</button>
            </div>
          </div>
          <div class="member">
            <div class="image">
              <img src={Member5} alt="" />
            </div>
            <div class="name-member">
              <h3>Sivapperujan</h3>
            </div>
            <div class="pro">
              <button className="numb">w1000000</button>
            </div>
          </div>
        </div>
      </div>
    </div>
    </>
  );
};

export default About;
