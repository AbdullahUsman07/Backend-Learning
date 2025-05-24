


import 'package:flutter/material.dart';

class CustomButton extends StatelessWidget {
   const CustomButton({
    super.key,
    required this.onPressed,
    required this.title,
  });

  final void Function()? onPressed;
  final String title;

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(  
      onPressed: onPressed,
      style: ElevatedButton.styleFrom(
        backgroundColor: Colors.purple,
        foregroundColor: Colors.black,
      ),
      child: Text(title),
    );
  }
}