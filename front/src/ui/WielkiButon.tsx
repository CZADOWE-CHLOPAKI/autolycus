const WielkiButon: React.FC = ({ children }) => (
  <button
    onClick={() => console.log('dupa')}
    className="flex flex-col text-white transition duration-700 transform rounded-sm group grow bg-gradient-to-r from-green-300 to-emerald-400 hover:skew-x-12 hover:-skew-y-6"
    style={{ fontFamily: 'BhuTuka Expanded One' }}
  >
    {children}

    <div className="group-hover:animate-spin-xslow group-hover:text-orange-600">
      <div className="text-xs text-right ">stara rure</div>
    </div>
  </button>
);

export default WielkiButon;
