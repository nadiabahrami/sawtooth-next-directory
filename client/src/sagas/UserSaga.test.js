import { call, put } from 'redux-saga/effects';


import FixtureAPI from '../services/FixtureApi';


import UserActions from '../redux/UserRedux';
import { me, getUser, getAllUsers } from '../sagas/UserSaga';


const stepper = (fn) => (mock) => fn.next(mock).value;
test('me API', () => {

  const step = stepper(me(FixtureAPI));
  expect(step()).toEqual(call(FixtureAPI.me));
});

test('me success path', () => {

  const res = FixtureAPI.me();
  const step = stepper(me(FixtureAPI, {

  }));

  step();

  const stepRes = step(res);
  expect(stepRes).toEqual(put(UserActions.meSuccess(res.data.data)));
});

test('failure path', () => {

  const res = { ok: false, data: {} };

  const step = stepper(me(FixtureAPI, {}));

  step();

  const stepRes = step(res);
  expect(stepRes).toEqual(put(UserActions.meFailure(res.data.error)));
});


test('getUser API', () => {
  const id = 'hello';

  const step = stepper(getUser(FixtureAPI, { id }));
  expect(step()).toEqual(call(FixtureAPI.getUser, id));
});

test('getUser success path', () => {
  const id = 'hello';

  const res = FixtureAPI.getUser(id);
  const step = stepper(getUser(FixtureAPI, {
    id: id,
  }));

  step();

  const stepRes = step(res);
  expect(stepRes).toEqual(put(UserActions.userSuccess(res.data.data)));
});

test('getUser failure path', () => {
  const res = { ok: false, data: {} };

  const id = 'hello';

  const step = stepper(getUser(FixtureAPI, {
    id: id,
  }));

  step();

  const stepRes = step(res);
  expect(stepRes).toEqual(put(UserActions.userFailure(res.data.error)));
});

test('getAllUsers success path', () => {
  const res = FixtureAPI.getUsers();
  const step = stepper(getAllUsers(FixtureAPI, {}));

  step();

  const stepRes = step(res);
  expect(stepRes).toEqual(put(UserActions.allUsersSuccess(res.data.data)));
});

test('getAllUsers failure path', () => {
  const res = { ok: false, data: {} };
  const step = stepper(getAllUsers(FixtureAPI, {}));

  step();

  const stepRes = step(res);
  expect(stepRes).toEqual(put(UserActions.allUsersFailure(res.data.data)));
});
