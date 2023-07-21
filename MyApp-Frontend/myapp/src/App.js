import React from 'react';
import { BrowserRouter, Route, Routes} from 'react-router-dom';
import Main from './pages/Main';
import StudyManagement from './pages/StudyManagement';
import ScheduleManagement from './pages/ScheduleManagement';
import ChoiceHelper from './pages/ChoiceHelper';

const App = () => {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route exact path="/" component={Main} />
          <Route path="/study" component={StudyManagement} />
          <Route path="/schedule" component={ScheduleManagement} />
          <Route path="/choice" component={ChoiceHelper} />
        </Routes>
      </BrowserRouter>
    </>
  );
};
export default App;