import 'package:flutter/material.dart';
import 'package:frontend/screens/mainscreen.dart';
import 'package:frontend/services/api_service.dart';
import 'package:frontend/widgets/customButton.dart';
import 'package:frontend/widgets/customTextFeild.dart';

class RegisterUserScreen extends StatefulWidget {
  const RegisterUserScreen({super.key});

  @override
  State<RegisterUserScreen> createState() => _RegisterUserScreenState();
}

class _RegisterUserScreenState extends State<RegisterUserScreen> {
  final TextEditingController nameController = TextEditingController();
  final TextEditingController passController = TextEditingController();
  final TextEditingController ageController = TextEditingController();
  final TextEditingController roleController = TextEditingController();

  @override
  void dispose() {
    nameController.dispose();
    passController.dispose();
    ageController.dispose();
    roleController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Register User'),
         centerTitle: true,
         backgroundColor: Theme.of(context).primaryColor,
         ),
      body: Padding(
        padding: const EdgeInsets.symmetric(vertical: 10, horizontal: 15),
        child: Center(
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
              const SizedBox(height: 10),
              CustomTextField(
                labelText: 'age',
                controller: ageController,
                keyboardType: TextInputType.number,
              ),
              const SizedBox(height: 10),
              CustomTextField(labelText: 'role', controller: roleController, keyboardType: TextInputType.text),
              const SizedBox(height: 20),
              CustomButton(onPressed: () async{
                final result = await ApiService.regsister(
                  nameController.text,
                  passController.text,
                  int.parse(ageController.text),
                  roleController.text,
                );
                if (!mounted) return;
                if (result != null) {
                  Navigator.pushAndRemoveUntil(
                    context,
                    MaterialPageRoute(builder: (context) => MainScreen(token: result['token'])),
                    (route)=>false,
                  );
                } else {
                  ScaffoldMessenger.of(context).showSnackBar(
                    const SnackBar(content: Text('Registration failed. Please try again.')),
                  );
                }
              }, title: 'Register'),
            ],
          ),
        ),
      ),
    );
  }
}
