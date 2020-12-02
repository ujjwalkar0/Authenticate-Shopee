import  React from 'react';
import {Text, View,Image,TextInput} from 'react-native';
import { MaterialIcons } from '@expo/vector-icons';
import { FontAwesome } from '@expo/vector-icons';
import { MaterialCommunityIcons } from '@expo/vector-icons';

export default class DLogin extends React.Component{
    constructor(){
        super()
        this.state= {
            showPass: true,
            press: false
        }
    }
    showPass=()=>{
        if(this.state.press== false){
            this.setState({ showPass: false, press: true})
        } else {
            this.setState({ showPass: true, press: false})
        }
    }
    render(){
        // const {navigate} = this.props.navigation
        return(
            <View style={{backgroundColor:"#FFF", height:"100%"}}>
                <Image source= {require('../images/customer.jpeg')}
                 style={{width:"100%",height:"40%"}}
                />
            <Text
            style={{
                fontSize:30,
                color:"#00716F",
                fontStyle:"normal",
                fontFamily:"semiBold",
                marginTop:20,
                alignSelf:"center",
            }}
            >Authenticate Shopee</Text>

            <Text
            style={{
                fontSize:20,
                fontFamily:"semiBold",
                marginHorizontal: 50,
                textAlign:'center',
                marginTop: 10,
                opacity:0.7
            }}
            >
            Delivery Boy Login
            </Text> 

            <View style={{
                flexDirection:"row",
                alignItems:"center",
                marginHorizontal:50,
                borderWidth:2,
                marginTop:30,
                paddingHorizontal:10,
                borderColor:"#00716F",
                borderRadius:23,
                paddingVertical:5
                }}>
                <FontAwesome name="user" size={24} color="lightseagreen" />
                
                <TextInput
                placeholder=" Your Email"
                autoCapitalize="none" 
                style={{paddingHorizontal:10,flex:1,fontSize:15}}
                />
            </View>

            <View style={{
                    flexDirection:"row",
                    alignItems:"center",
                    marginHorizontal:50,
                    borderWidth:2,
                    marginTop:20,
                    paddingHorizontal:10,
                    borderColor:"#00716F",
                    borderRadius:23,
                    paddingVertical:5
                }}>
                <MaterialIcons name="lock" size={24} color="lightseagreen" />
             <TextInput 
                secureTextEntry={this.state.showPass}
                placeholder="Your Password               "
                autoCapitalize="none" 
                style={{paddingHorizontal:10,flex:1,fontSize:15}}
                />
                <MaterialCommunityIcons onPress={this.showPass.bind(this)} 
                name={this.state.press== false ?'eye-off' : 'eye'}
                size={24} 
                color="lightseagreen" />
                </View>

                <View style={{
                    marginHorizontal:50,
                    alignItems:"center",
                    justifyContent:"center",
                    marginTop:40,
                    backgroundColor:"#00716F",
                    paddingVertical:10,
                    borderRadius:23
                }}>
                    <Text style={{
                    color:"white",
                    fontFamily:"semiBold",
                    fontStyle:"normal",
                    fontSize:20,
                    }}>Already a member</Text>
                </View>

                <Text 
                onPress={()=>navigate('DeliveryboyRegister')}
                style={{
                    alignSelf:"center",
                    fontFamily:"semiBold",
                    fontStyle:"normal",
                    fontSize:15,
                    paddingVertical:30
                }}>New Delivery Boy
                </Text>
            </View>
        )
    }
}