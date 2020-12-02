import  React from 'react';
import {Text, View,Image,TextInput} from 'react-native';
import { MaterialIcons } from '@expo/vector-icons';
import { MaterialCommunityIcons } from '@expo/vector-icons';


export default class SRegister extends React.Component{
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
        return(
            <View style={{backgroundColor:"#FFF", height:"100%"}}>
                <Image source= {require('../images/customer.jpeg')}
                 style={{width:"100%",height:"40%"}}
                />
            <Text
            style={{
                fontSize:30,
                fontFamily:"semiBold",
                marginTop:10,
                alignSelf:"center",
            }}
            >Authenticate Shopee</Text>

            <Text
            style={{
                fontFamily:"semiBold",
                marginHorizontal: 50,
                textAlign:'center',
                marginTop: 4,
                opacity:0.7
            }}
            >
            Shopowner Register
            </Text> 
            <View style={{
                flexDirection:"row",
                alignItems:"center",
                marginHorizontal:55,
                borderWidth:2,
                marginTop:30,
                paddingHorizontal:10,
                borderColor:"#00716F",
                borderRadius:23,
                paddingVertical:3
                }}>
                
                <TextInput
                placeholder="First Name"
                placeholderTextColor="#00716F"
                style={{paddingHorizontal:10}}
                />
            </View>
            <View style={{
                flexDirection:"row",
                alignItems:"center",
                marginHorizontal:55,
                borderWidth:2,
                marginTop:15,
                paddingHorizontal:10,
                borderColor:"#00716F",
                borderRadius:23,
                paddingVertical:3
                }}>
                
                <TextInput
                placeholder="Last Name"
                placeholderTextColor="#00716F"
                style={{paddingHorizontal:10}}
                />
            </View>
            <View style={{
                flexDirection:"row",
                alignItems:"center",
                marginHorizontal:55,
                borderWidth:2,
                marginTop:15,
                paddingHorizontal:10,
                borderColor:"#00716F",
                borderRadius:23,
                paddingVertical:3
                }}>
                
                <TextInput
                placeholder="Email"
                placeholderTextColor="#00716F"
                style={{paddingHorizontal:10}}
                />
            </View>
            <View style={{
                    flexDirection:"row",
                    alignItems:"center",
                    marginHorizontal:55,
                    borderWidth:2,
                    marginTop:15,
                    paddingHorizontal:10,
                    borderColor:"#00716F",
                    borderRadius:23,
                    paddingVertical:3
                }}>
                
                <TextInput
                    secureTextEntry={this.state.showPass}
                    placeholder="Password                                            "
                    placeholderTextColor="#00716F"
                    
                    style={{paddingHorizontal:10}}
                />
                <MaterialCommunityIcons onPress={this.showPass.bind(this)} 
                name={this.state.press== false ?'eye-off' : 'eye'} 
                size={24} 
                color="lightseagreen" />
                </View>
                <View style={{
                    flexDirection:"row",
                    alignItems:"center",
                    marginHorizontal:55,
                    borderWidth:2,
                    marginTop:15,
                    paddingHorizontal:10,
                    borderColor:"#00716F",
                    borderRadius:23,
                    paddingVertical:2
                }}>
                   
                <TextInput 
                    secureTextEntry={this.state.showPass}
                    placeholder="Confirm Password                             "
                    placeholderTextColor="#00716F"
                    
                    style={{paddingHorizontal:10}}
                /><MaterialCommunityIcons onPress={this.showPass.bind(this)} 
                name={this.state.press== false ?'eye-off' : 'eye'} 
                size={24} 
                color="lightseagreen" />
                    

                </View>
                <View style={{
                    marginHorizontal:55,
                    alignItems:"center",
                    justifyContent:"center",
                    marginTop:30,
                    backgroundColor:"#00716F",
                    paddingVertical:10,
                    borderRadius:23
                }}>
                    <Text style={{
                    color:"white",
                    fontFamily:"semiBold"
                    }}>Register</Text>
                </View>
                

            
            </View>
        )
    }
}