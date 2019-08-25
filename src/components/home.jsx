import React, { useState } from "react";
import "./home.scss";

const Home = () => {
  const [loading, setLoading] = useState(false);
  const [btnClassName, setbtnClassName] = useState("create-btn");
  const [formClassName, setformClassName] = useState("form");

  const handleCreate = () => {
    setLoading(!loading);
    if (btnClassName === "create-btn") {
      setbtnClassName("create-btn expand");
      setformClassName("form collapsed");
    } else {
      setbtnClassName("create-btn");
      setformClassName("form expanded");
    }
  };

  return (
    <div id="home-container">
      <div id="navbar">
        <p>
          React <span>Initializr</span>
        </p>
      </div>

      <div className={formClassName}>
        <p>Nuevo proyecto React.js</p>
        <div className="input">
          <fieldset>
            <legend>Nombre del proyecto</legend>
            <input type="text" />
          </fieldset>
        </div>

        <div className="input">
          <fieldset>
            <legend>Ruta del proyecto</legend>
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

      <div className="console">
        <div className="console-header">
          <p>proyectautomate.py</p>
          <p>index.html</p>
        </div>
        <p>
          Compiled successfully! <br /> <br /> You can now view reactinitializr
          in the browser. <br /> Local: http://localhost:3000/ <br /> On Your
          Network: http://192.168.56.1:3000/ <br /> <br /> Note that the
          development build is not optimized. To create a production build, use
          npm run build.
        </p>
      </div>
    </div>
  );
};

export default Home;
