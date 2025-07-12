<script lang="js">
  import { clsx } from 'clsx';
  let { class: className, children, variant = 'accent', ...restProps } = $props();
  const baseClasses =
    'inline-flex rounded-lg px-5 py-3 text-sm lg:text-base font-medium  items-center justify-center';
  const transitionClasses = 'hover:transition-colors hover:duration-300 hover:delay-150';
  const variantClasses = {
    accent: 'bg-indigo-600 text-gray-200 hover:bg-indigo-500 hover:text-white',
    clear: 'text-indigo-600 hover:text-indigo-500 dark:text-gray-200 dark:hover:text-white'
  };
</script>

<button
  class={clsx(baseClasses, variantClasses[variant], className, transitionClasses)}
  {...restProps}>{@render children()}</button
>
