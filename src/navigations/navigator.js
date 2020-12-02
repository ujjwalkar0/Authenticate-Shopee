// import {createStackNavigator} from 'react-navigation-stack';
// import {createAppContainer} from 'react-navigation';
import CLogin from '../screens/CustomerLogin';
import CRegister from '../screens/CustomerRegister';
import SLogin from '../screens/ShopownerLogin';
import SRegister from '../screens/ShopownerRegister';
import DLogin from '../screens/DeliveryboyLogin';
import DRegister from '../screens/DeliveryboyRegister';
import Front from '../screens/Frontpage';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import React from 'react'


const stackNavigatorOptions = {
    headerShown:false
}
// const AppNavigator = createStackNavigator({
    // DeliveryboyLogin:{screen: DLogin},
    /*Register:{screen:Register},*/

function AppNavigator(){
    return (
    <>
    <BrowserRouter>
    <Switch>
    <Route path="/"><Front /></Route>
    <Route path="/CLogin"><CLogin /></Route>
    <Route path="/CRegister"><CRegister /></Route>
    <Route path="/SLogin"><SLogin /></Route>
    <Route path="/SRegister"><SRegister /></Route>
    <Route path="/DLogin"><DLogin /></Route>
    <Route path="/DRegister"><DRegister /></Route>
    </Switch>
    </BrowserRouter>
    </>
)
}
export default AppNavigator;