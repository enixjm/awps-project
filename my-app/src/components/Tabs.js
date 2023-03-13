import { useState } from 'react';
import { Grid, Tabs, Tab, Box } from '@mui/material';

import BarChart from "./BarChart";
import LineChart from "./LineChart";
import PieChart from "./PieChart";
import { UserData } from "./Data";
import { useEffect } from "react";

import ListDividers from "./Stacks_Lan"

function MyTabs() {
  const [value, setValue] = useState(0);
  const [subvalue, setSubValue] = useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  const handleSubChange = (event, newSubValue) => {
    setSubValue(newSubValue);
  };
  const [userData, setUserData] = useState({
      labels: UserData.map((data) => data.year),
      datasets: [
          {
          label: "Users Gained",
          data: UserData.map((data) => data.userGain),
          backgroundColor: [
              "rgba(75,192,192,0.7)",
              "rgba(97,61,248,0.73)",
              "rgba(80,175,149,0.71)",
              "rgba(243,186,47,0.75)",
              "rgba(42,113,208,0.75)",
          ],
          borderColor: "rgba(255, 99, 132, 0.2)",
          borderWidth: 2,
          },
      ],
  });


  return (
    <Box sx={{
      width: '80%'
    }}>
      <Tabs
        value={value}
        onChange={handleChange}
        centered
        sx={{bgcolor:'8a61fb'}}
        >
        <Tab label="기술&스택" />
        <Tab label="급여" />
        <Tab label="근무 지역" />
        <Tab label="평균 재직기간" />
        <Tab label="요구 경력"/>
      </Tabs>
      {value === 0 && (
        <Box>
          <Tabs
            value={subvalue}
            onChange={handleSubChange}
            centered
            sx={{ bgcolor: "8a61fb" }}
          >
            <Tab label="언어" />
            <Tab label="프레임워크" />
            <Tab label="개발" />
            <Tab label="test" />
          </Tabs>
          <Box  sx={{ width: "100%", height: "500px" }}>
          {subvalue === 0 && <ListDividers/>}
          {subvalue === 1 && <LineChart chartData={userData}/>}
          {subvalue === 2 && <PieChart chartData={userData}/>}
          {subvalue === 3 && <BarChart chartData={userData}/>}
          </Box>
        </Box>
      )}

      {value === 1 && (
        <Box>
          <Tabs
            value={subvalue}
            onChange={handleSubChange}
            centered
            sx={{ bgcolor: "8a61fb" }}
          >
            <Tab label="Front" />
            <Tab label="Back" />
          </Tabs>
      {value === 2 && <PieChart chartData={userData}/>}
        </Box>
      )}
    </Box>
  );
}

export default MyTabs;