/**
 * Extracts the weekday from a date string
 * @param dateString - The date string to extract the weekday from
 * @returns The weekday of the date
 */
export const extractWeekday = (dateString: string) => {
  const date = new Date(dateString);

  if (isNaN(date.getTime())) {
    return "";
  }

  return date.toLocaleDateString("en-US", { weekday: "long" });
};

/**
 * Format date string to a more human readable way: day - month - year - hour - minute
 * @param dateString - The date string to format
 * @returns date string formatted as day - month - year - hour - minute
 */
export const formatDate = (dateString: string) => {
  const date = new Date(dateString);
  return date.toLocaleDateString("en-US", {
    day: "numeric",
    month: "short",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
};
