import { useEffect, useState } from "react";
import { on, off } from "./lib/utils";
export interface BatteryState {
  charging: boolean;
  chargingTime: number;
  dischargingTime: number;
  level: number;
}

interface BatteryManager extends Readonly<BatteryState>, EventTarget {
  onchargingchange?: () => void;
  onchargingtimechange?: () => void;
  ondischargingtimechange?: () => void;
  onlevelchange?: () => void;
}

interface Nav extends Navigator {
  getBattery?: () => Promise<BatteryManager>;
}

type useBatteryState =
  | { isSupported: false }
  | { isSupported: true; fetched: false }
  | (BatteryState & { isSupported: true; fetched: true });

export function useBattery() {
  const [battery, setBattery] = useState<useBatteryState>({
    isSupported: true,
    fetched: false
  });
  const nav: Nav = window.navigator;

  useEffect(() => {
    let isMounted = true;
    let batStat: BatteryManager;

    function handleChange() {
      if (!isMounted) return;

      const bat: useBatteryState = {
        isSupported: true,
        fetched: true,
        charging: batStat?.charging,
        level: batStat?.level,
        dischargingTime: batStat?.dischargingTime,
        chargingTime: batStat?.chargingTime
      };
      if (JSON.stringify(bat) !== JSON.stringify(battery)) {
        setBattery(bat);
      }
    }

    nav?.getBattery?.().then((bat) => {
      batStat = bat;
      on(batStat, "chargingchange", handleChange);
      on(batStat, "chargingtimechange", handleChange);
      on(batStat, "dischargingtimechange", handleChange);
      on(batStat, "levelchange", handleChange);
      handleChange();
    });

    return () => {
      isMounted = false;
      if (batStat) {
        off(batStat, "chargingchange", handleChange);
        off(batStat, "chargingtimechange", handleChange);
        off(batStat, "dischargingtimechange", handleChange);
        off(batStat, "levelchange", handleChange);
      }
    };
  }, []);

  return battery;
}