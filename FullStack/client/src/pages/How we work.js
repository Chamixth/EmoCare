import React from "react";
import PickMeals from "../Assets/pick-meals-image.png";
import ChooseMeals from "../Assets/choose-image.png";
import DeliveryMeals from "../Assets/delivery-image.png";
import Navbar from "./Navbar";

const Work = () => {
  const workInfoData = [
    {
      image: PickMeals,
      title: "Video Therapy Sessions",
      text: "Lorem ipsum dolor sit amet consectetur. Maecenas orci et sagittis duis elementum interdum facilisi bibendum.",
    },
    {
      image: ChooseMeals,
      title: "Schedule Your Therapist",
      text: "You can make an appointment with our theraphist by checking our list.",
    },
    {
      image: DeliveryMeals,
      title: "Support Till The End",
      text: "Our program will stay with you till the end.",
    },
  ];
  return (
    <>
      < Navbar />

    <div className="work-section-wrapper">
      <div className="work-section-top">
        <h1 className="primary-heading-1">How We Work</h1>
        <p className="primary-text">
          We are here to help you. You can get below services from us. We are
          always happy to help you.
        </p>
      </div>
      <div className="work-section-bottom">
        {workInfoData.map((data) => (
          <div className="work-section-info" key={data.title}>
            <div className="info-boxes-img-container card">
              <img src={data.image} alt="" />
            </div>
            <h2>{data.title}</h2>
            <p>{data.text}</p>
          </div>
        ))}
      </div>
    </div>
    </>
  );
};

export default Work;
