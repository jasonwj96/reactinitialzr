import React, { useState } from "react";
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

      <div className="form">
        <p>Nuevo proyecto React.js</p>
        <div className="input">
          <fieldset>
            <legend>Nombre del proyecto</legend>
            <input type="text" />
          </fieldset>
        </div>

        <div className="input">
          <fieldset>
            <legend>Nombre del repositorio Github</legend>
            <input type="text" />
          </fieldset>
        </div>

        <div className="input">
          <fieldset>
            <legend>Usuario Github</legend>
            <input type="text" />
          </fieldset>
        </div>

        <div className="input">
          <fieldset>
            <legend>Contraseña Github</legend>
            <input type="password" />
          </fieldset>
        </div>
      </div>

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
            <p>Crear proyecto</p>
          )}
        </div>
      </button>
      {/* 
      <div className="console">
        <p>Console</p>
      </div> */}
    </div>
  );
};

export default Home;
