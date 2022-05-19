import { useMemo, useState } from 'react';
import CryingLaughSrc from './assets/crying_laugh.png';
import RedditSettings from './RedditSettings';
import useRandomCryingEmoji from './ui/useRandomCryingEmoji';
import WielkiButon from './ui/WielkiButon';
import VideoWrapper from './VideoWrapper';

const generateRandomCryingEmoji = (count: number, hidden: boolean) => {
  return (
    <div
      className="w-0 h-0 overflow-hidden pointer-events-none"
      hidden={hidden}
    >
      {Array.from(Array(count).keys()).map((e, index) => {
        const width = `${Math.floor(Math.random() * 50)}px`;
        return (
          <img
            key={index}
            className="absolute w-10 animate-spin-slow"
            style={{
              top: `${Math.floor(Math.random() * 100)}vh`,
              left: `${Math.floor(Math.random() * 100)}vw`,
              width,
            }}
            src={CryingLaughSrc}
          />
        );
      })}
    </div>
  );
};

function App() {
  const [renderCryingEmojiSlider, renderRandomCryingEmoji, toggleEmoji] =
    useRandomCryingEmoji();

  return (
    <div>
      <div className="grid w-screen h-screen space-y-32 text-3xl bg-indigo-200 place-content-center">
        <div onMouseOver={() => toggleEmoji(true)}>
          <WielkiButon>
            przycisk gigantyczny wielki ze potezny i mozna wygenerowac filmik
            fajny po prostu a okej
          </WielkiButon>
        </div>
        <RedditSettings />
        {renderCryingEmojiSlider()}
      </div>
      <div className="grid w-screen h-screen place-content-center">
        <VideoWrapper />
      </div>
      {renderRandomCryingEmoji()}
    </div>
  );
}

export default App;
