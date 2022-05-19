type NormalButtonProps = {
  onClick: () => any;
  isLoading?: boolean;
  loadingText: string;
};

const NormalButton: React.FC<NormalButtonProps> = ({
  children,
  onClick,
  isLoading,
  loadingText,
}) => (
  <div>
    <button
      onClick={onClick}
      className="flex flex-col p-2 text-white bg-gray-500 border-2 border-white "
    >
      {children}
    </button>
    {isLoading && (
      <div className="w-0 h-0 animate-spin-slow">{loadingText}</div>
    )}
  </div>
);

export default NormalButton;
