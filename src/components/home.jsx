import React, { useEffect, useState } from "react";
import "./home.scss";

const Home = () => {
  const [loading, setLoading] = useState(false);
  const [btnClassName, setbtnClassName] = useState("create-btn");

  const handleCreate = () => {
    setLoading(!loading);
    if (btnClassName === "create-btn") {
      setbtnClassName("create-btn expand");
    } else {
      setbtnClassName("create-btn");
    }
  };

  return (
    <div id="home-container">
      <div id="navbar">
        <p>
          React <span>Initializr</span>
        </p>
      </div>

      <div className="form"></div>

      <button
        id="create-button"
        className={btnClassName}
        onClick={handleCreate}
      >
        <div id="btn-element">
          {loading ? (
            <div className="loading-msg">
              <i className="fas fa-cog" />
              <p>Creando</p>
              <div>.</div>
              <div>.</div>
              <div>.</div>
            </div>
          ) : (
            <p>Crear</p>
          )}
        </div>
      </button>

      <div className="console">
        <p>Console</p>
      </div>
    </div>
  );
};

export default Home;
