import React from "react";
import { Link } from "react-router-dom";

export default function Home() {
  return (
    <main>
      <WenM />
      <Features />
    </main>
  );
}

const WenM = () => (
  <section className="wenM">
    <div className="wenM__content">
      <h1 className="wenM__title">RoboDux</h1>
      <p className="wenM__subtitle">Start manipulating the robot using the artboard!</p>

      <Link to="/sketch">Drawing right now</Link>
    </div>
  </section>
);


function Features() {
  const featuresData = [
    {
      heading: "Organic & Ethical",
      text:
        "An extra arm to boost your career!",
      img: { src: "./DuckRo.png", alt: "DuckRo" }
    },
    {
      heading: "Live Entertainment",
      text:
        "Allows you to complete signatures thousands of miles away in the office!",
      img: {
        src: './Roduck.png',
        alt: "Roduck"
      }
    },
    {
      heading: "Satisfaction guaranteed",
      text:
        "You draw the pattern you want and the machine will make it a reality!",
      img: { src: "./Robowrite.png", alt: "Robowrite" }
    }
  ];

  return (
    <article className="features">
      <div className="features__header">
        <h2>Let robot print your drawing!</h2>
      </div>

      <div className="features__box-wrapper">
        {
          featuresData.map((feature) => (
            <FeatureBox feature={feature} />
          ))
        }
      </div>
    </article>
  );
}

const FeatureBox = ({ feature }) => (
  <div className="features__box">
    <img src={feature.img.src} alt={feature.img.alt} />
    <h5>{feature.title}</h5>
    <p>{feature.text}</p>
  </div>
);
