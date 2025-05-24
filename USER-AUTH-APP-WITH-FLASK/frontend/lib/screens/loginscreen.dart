import 'package:flutter/material.dart';
import 'package:frontend/screens/mainscreen.dart';
import 'package:frontend/services/api_service.dart';
import 'package:frontend/widgets/customButton.dart';
import 'package:frontend/widgets/customTextFeild.dart';

class LoginUserScreen extends StatefulWidget {
  const LoginUserScreen({super.key});

  @override
  State<LoginUserScreen> createState() => _LoginUserScreenState();
}

class _LoginUserScreenState extends State<LoginUserScreen> {
  final TextEditingController nameController = TextEditingController();
  final TextEditingController passController = TextEditingController();

  @override
  void dispose() {
    nameController.dispose();
    passController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Login User'),
        centerTitle: true,
        backgroundColor: Theme.of(context).primaryColor,
      ),
      body: Padding(
        padding: const EdgeInsets.symmetric(vertical: 10, horizontal: 15),
        child: ListView(
          children: [
            CustomTextField(
              labelText: 'username',
              controller: nameController,
              keyboardType: TextInputType.text,
            ),
            const SizedBox(height: 10),
            CustomTextField(
              labelText: 'password',
              controller: passController,
              keyboardType: TextInputType.text,
              isPassword: true,
            ),
            const SizedBox(height: 20),
            CustomButton(onPressed: () async{
              final result = await ApiService.login(
                nameController.text,
                passController.text,
              );
              if(!mounted) return;
              if(result != null){
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(content: Text('Login successful!')),
                );
                Navigator.pushAndRemoveUntil(
                  context,
                  MaterialPageRoute(builder: (context) => MainScreen(token: result['token'])),
                  (route)=> false,
                );
              }else{
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(content: Text('Login failed. Please try again.')),
                );
              }
            }, title: 'Login'),
          ],
        ),
      ),
    );
  }
}
