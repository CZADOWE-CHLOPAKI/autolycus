import { useState } from 'react';
import NormalButton from './ui/NormalButton';
import { createAndGetVideoBlob } from './utils/api';

const VideoWrapper = () => {
  const [videoUrl, setVideoUrl] = useState<string>();
  const [isGeneratingVideo, setIsGeneratingVideo] = useState(false);

  const generateVideo = async () => {
    setIsGeneratingVideo(true);

    const blob = await createAndGetVideoBlob('memes');

    setVideoUrl(URL.createObjectURL(blob));
    setIsGeneratingVideo(false);
  };

  return (
    <div>
      <NormalButton
        onClick={() => generateVideo()}
        isLoading={isGeneratingVideo}
        loadingText="generuje film..."
      >
        zrub film z memow
      </NormalButton>
      <div>
        {videoUrl && (
          <video
            controls
            autoPlay={true}
            src={videoUrl}
            width={300}
            height={500}
          />
        )}
      </div>
    </div>
  );
};

export default VideoWrapper;
