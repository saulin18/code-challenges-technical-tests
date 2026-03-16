export const ChevronDownIcon: React.FC<React.SVGProps<SVGSVGElement>> = ({
  ...props
}) => {
  return (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    fill="none"
    viewBox="0 0 24 24"
    stroke="currentColor"
    strokeWidth={2}
    strokeLinecap="round"
    strokeLinejoin="round"
    {...props}
  >
    <path d="M19 9l-7 7-7-7" />
  </svg>
  );
};
