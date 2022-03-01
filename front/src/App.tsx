import { FC, useState } from 'react';
import CryingLaughSrc from './assets/crying_laugh.png';

function App() {
  const [textValue, setTextValue] = useState('memes');
  const [showCryingEmoji, setShowCryingEmoji] = useState(false);

  const generateRandomCryingEmoji = (count: number) => {
    return Array(45).map((_, key) => {
      const position = {
        x: Math.floor(Math.random() * window.screen.width),
        y: Math.floor(Math.random() * window.screen.height),
      };
      return (
        <img
          key={key}
          className="absolute w-10 animate-spin-slow"
          style={{
            top: position.y,
            left: position.x,
          }}
          src={CryingLaughSrc}
        />
      );
    });
  };

  const generujElegenackoNumerkiLosowe = () => {
    return {
      x: Math.floor(Math.random() * window.screen.width),
      y: Math.floor(Math.random() * window.screen.height),
    };
  };

  return (
    <div className="grid w-screen h-screen space-y-32 text-3xl bg-indigo-200 place-content-center">
      <div onMouseOver={() => setShowCryingEmoji(true)}>
        <WielkiButon />
      </div>
      {/* {Array.from(Array(10).keys()).map((e) => {
        return generateRandomCryingEmoji();
      })} */}
      <div className="flex items-center justify-center space-x-2 ">
        <div>r/</div>
        <input
          className="-skew-x-6 bg-transparent border-4 border-purple-600 focus:outline-none"
          type="text"
          value={textValue}
          onChange={(e) => setTextValue(e.target.value)}
        />
      </div>
      <div className="overflow-hidden" hidden={!showCryingEmoji}>
        {Array.from(Array(100).keys()).map((e, index) => {
          const width = `${Math.floor(Math.random() * 50)}px`;
          return (
            <img
              key={index}
              className="absolute w-10 animate-spin-slow"
              style={{
                top: `${Math.floor(Math.random() * 95)}vh`,
                left: `${Math.floor(Math.random() * 95)}vw`,
                width,
              }}
              src={CryingLaughSrc}
            />
          );
        })}
      </div>
    </div>
  );
}

export default App;

// const WielkiButon = () => (
//   <button onClick={() => console.log('dupa')} className="transform group">
//     <div className="p-4 font-mono text-white duration-200 transform bg-purple-600 rounded font-extralight group-hover:rotate-6 group-hover:skew-x-12 ">
//       wielki przycisk co mozna nim wygenerowac film smieszny do smiania sie duzo
//       ubaw po pachy
//     </div>
//   </button>
// );

const WielkiButon = () => (
  <button
    onClick={() => console.log('dupa')}
    className="flex flex-col text-white transition duration-700 transform rounded-sm group grow bg-gradient-to-r from-green-300 to-emerald-400 hover:skew-x-12 hover:-skew-y-6"
    style={{ fontFamily: 'BhuTuka Expanded One' }}
  >
    <div>
      przycisk gigantyczny wielki ze potezny i mozna wygenerowac filmik fajny po
      prostu a okej
    </div>
    <div className="group-hover:animate-spin-xslow group-hover:text-orange-600">
      <div className="text-xs text-right ">stara rure</div>
    </div>
  </button>
);
