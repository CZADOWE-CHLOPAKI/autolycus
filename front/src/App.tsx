import RedditSettings from './RedditSettings';
import { useRandomCryingEmoji } from './ui/useRandomCryingEmoji';
import WielkiButon from './ui/WielkiButon';
import VideoWrapper from './VideoWrapper';

function App() {
  const [renderCryingEmojiSlider, renderRandomCryingEmoji, toggleEmoji] =
    useRandomCryingEmoji();

  return (
    <div>
      <div className="grid w-screen h-screen space-y-32 text-3xl bg-indigo-200 place-content-center">
        <div onMouseOver={() => toggleEmoji()}>
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
