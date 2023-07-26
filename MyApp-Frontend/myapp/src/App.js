import React from 'react';
import { BrowserRouter, Route, Routes} from 'react-router-dom';
import Main from './pages/Main';
import StudyManagement from './pages/StudyManagement';
import ScheduleManagement from './pages/ScheduleManagement';
// import ChoiceHelper from './pages/ChoiceHelper';
import CourseManagement from './pages/CourseManagement';
import SubjectManagement from './pages/SubjectManagement';
import TestManagement from './pages/TestManagement';

const App = () => {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route exact path="/" element={<Main />} />
          <Route path="/study" element={<StudyManagement />} />
          <Route path="/schedule" element={<ScheduleManagement />} />
          {/* <Route path="/choice" element={<ChoiceHelper />} /> */}
          <Route path="/course" element={<CourseManagement />} />
          <Route path="/subject" element={<SubjectManagement />} />
          <Route path="/test" element={<TestManagement />} />
          <Route path="*" element={<h1>Not Found</h1>} />
        </Routes>
      </BrowserRouter>
    </>
  );
};
export default App;