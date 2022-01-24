import { useState } from 'react';

function App() {
  const [textValue, setTextValue] = useState('memes');
  return (
    <div className="grid w-screen h-screen space-y-32 text-3xl bg-blue-400 place-content-center">
      <LargeButton />

      <div className="flex items-center justify-center space-x-2 text-white">
        <div className="">r/</div>
        <input
          className="-skew-x-6 bg-transparent border-4 border-purple-600 focus:outline-none"
          type="text"
          value={textValue}
          onChange={(e) => setTextValue(e.target.value)}
        />
      </div>
    </div>
  );
}

export default App;

const LargeButton = () => (
  <button onClick={() => console.log('dupa')} className="transform group">
    <div className="p-4 font-mono text-white duration-200 transform bg-purple-600 rounded font-extralight group-hover:rotate-6 group-hover:skew-x-12 ">
      wielki przycisk co mozna nim wygenerowac film smieszny do smiania sie duzo
      ubaw po pachy
    </div>
  </button>
);
