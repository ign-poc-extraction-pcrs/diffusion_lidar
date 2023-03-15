import { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [data, setData] = useState({});

  useEffect(() => {
    axios.get("http://api:8000/hello_world").then((response) => {
      setData(response.data);
    });
  }, []);

  return (
    <div>
      <h1>{data.hello}</h1>
    </div>
  );
}

export default App;
