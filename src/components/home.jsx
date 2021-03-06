import React, { useState } from "react";
import "./home.scss";

const Home = () => {
  const [loading, setLoading] = useState(false);
  const [btnClassName, setbtnClassName] = useState("create-btn");
  const [formClassName, setformClassName] = useState("form expanded");
  const [consoleClassName, setconsoleClassName] = useState("console collapsed");

  const handleCreate = () => {
    setLoading(!loading);
    if (!loading) {
      setbtnClassName("create-btn expand-btn");
      setformClassName("form collapsed");
      setconsoleClassName("console expanded");
    } else {
      setbtnClassName("create-btn");
      setformClassName("form expanded");
      setconsoleClassName("console collapsed");
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

      <div className={consoleClassName}>
        <div className="console-header">
          <p>proyectautomate.py</p>
          <p>index.html</p>
        </div>
        <div className="prompt">
          <p>
            <p className="success-msg">Compiled successfully!</p>
            <p className="msg">
              You can now view reactinitializr in the browser.
            </p>
            <p className="info-msg">Local: http://localhost:3000/</p>
            <p className="info-msg">
              On Your Network: http://192.168.56.1:3000/
            </p>
            <p className="msg">
              Note that the development build is not optimized. To create a
              production build, use npm run build.
            </p>
          </p>
        </div>
      </div>
    </div>
  );
};

export default Home;
