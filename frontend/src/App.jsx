import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [value, setValue] = useState("Loading...");
  const [value2, setValue2] = useState({
    sizes: [],
    bedrooms: [],
  });
  const [price, setPrice] = useState("");

  const fetchValue = async () => {
    try {
      const res = await axios.post(
        "http://localhost:5000/api/predict/",
        value2
      );
      // setValue(res.data)
      console.log(res.data.results[0].predicted_price);
      setPrice(res.data.results[0].predicted_price);
    } catch (error) {
      console.log(error.message);
    }
  };

  return (
    <>
      <h1 className="text-5xl mt-10 font-bold text-primary">
        Welcome to House Price Prediction
      </h1>
      <div className="flex gap-4 mt-4">
        <input
          type="number"
          value={value2.sizes}
          placeholder="Enter Size"
          className="input input-bordered input-accent w-full max-w-xs"
          onChange={(e) =>
            setValue2({ ...value2, sizes: [Number(e.target.value)] })
          }
        />
        <input
          type="number"
          value={value2.bedrooms}
          placeholder="Enter bedrrom"
          className="input input-bordered input-accent w-full max-w-xs"
          onChange={(e) =>
            setValue2({ ...value2, bedrooms: [Number(e.target.value)] })
          }
        />
        <button className="btn btn-accent" onClick={fetchValue}>
          Predict
        </button>
      </div>
      <div className="flex items-center w-full" >
        <h1 className="text-5xl mt-10 font-bold underline">
          {`Predicted Price: ${price}`}
        </h1>
      </div>
    </>
  );
}

export default App;
